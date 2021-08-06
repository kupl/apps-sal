class axis:
    def __init__(self, lilies):
        self.line = lilies


class frog:
    def __init__(self, d, my_axis):
        self.axis = my_axis
        self.d = d
        self.point = 0

    def jump(self):
        for i in range(self.point + self.d, self.point, -1):
            if i >= len(self.axis.line):
                continue

            if self.axis.line[i] == '1':
                self.point = i
                return True

        return False


n, d = [int(i) for i in input().split()]
lilies = input().strip()

my_axis = axis(lilies)
my_frog = frog(d, my_axis)

jump_count = 0

while my_frog.point < n - 1:
    if my_frog.jump():
        jump_count += 1
    else:
        jump_count = -1
        break

print(jump_count)
