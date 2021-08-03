def solve(a):
    b = sorted(a)
    if len(b) % 2:
        return "Second"
    else:
        if b[::2] == b[1::2]:
            return "Second"
        else:
            return "First"


for _ in range(int(input())):
    input()
    print(solve(list(map(int, input().split()))))
