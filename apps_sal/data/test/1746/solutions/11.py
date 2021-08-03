n = int(input())
p = [int(input()) for i in range(n - 1)]

c_children = [0] * (n + 1)

for pi in p:
    c_children[pi] += 1


def is_leaf(i):
    return c_children[i] == 0


for i in range(1, n + 1):
    if not is_leaf(i):
        t = 0

        for j in range(2, n + 1):
            if p[j - 2] == i and is_leaf(j):
                t += 1

        if t < 3:
            print("No")
            return

print("Yes")
