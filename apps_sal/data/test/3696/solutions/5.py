
import sys

n = int(sys.stdin.readline().split()[0])


class Polynomial:
    def __init__(self, coef):
        first_nonzero = False
        index = len(coef) - 1
        while not first_nonzero:
            if not coef[index] == 0:
                first_nonzero = True
            else:
                if index == 0:
                    first_nonzero = True
                else:
                    index -= 1
        self.degree = index
        self.coef = [coef[j] for j in range(index + 1)]

    def multiply_by_x(self):
        new_coef = [0]
        for j in range(self.degree + 1):
            new_coef.append(self.coef[j])
        return Polynomial(new_coef)

    def minus(self):
        new_coef = [-self.coef[j] for j in range(self.degree + 1)]
        return Polynomial(new_coef)

    def add(self, other):
        other_coef = other.coef
        new_coef = [0 for j in range(max(self.degree, other.degree) + 1)]
        m = min(self.degree, other.degree)
        M = max(self.degree, other.degree)
        if self.degree > other.degree:
            bigger_poly = self
        else:
            bigger_poly = other
        for j in range(m + 1):
            new_coef[j] = self.coef[j] + other.coef[j]
        for j in range(m + 1, M + 1):
            new_coef[j] = bigger_poly.coef[j]

        return Polynomial(new_coef)

    def is_legal(self):
        result = True
        bools = [None for j in range(self.degree + 1)]
        bools[self.degree] = self.coef[self.degree] == 1
        for j in range(self.degree):
            bools[j] = self.coef[j] == 0 or self.coef[j] == 1 or self.coef[j] == -1
        for j in range(self.degree + 1):
            result = result and bools[j]
        return result

    def print(self):
        output = ""
        for j in range(self.degree + 1):
            output += str(self.coef[j]) + " "
        print(output)


f = []

f.append(Polynomial([1]))
f.append(Polynomial([0, 1]))

for j in range(2, 151):
    xf = f[j - 1].multiply_by_x()
    t_1 = xf.add(f[j - 2])
    t_2 = xf.add(f[j - 2].minus())
    if t_1.is_legal():
        f.append(t_1)
    elif t_2.is_legal():
        f.append(t_2)
    # print(":(")


print(f[n].degree)
f[n].print()
print(f[n - 1].degree)
f[n - 1].print()

# for j in range(len(f)):
# f[j].print()
