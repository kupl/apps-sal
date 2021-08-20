def solve(s):
    return '+'.join(map(str, sorted(list(map(int, s.split('+'))))))


tmp = input()
print(solve(tmp))
