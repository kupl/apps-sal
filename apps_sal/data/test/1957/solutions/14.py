n, A, B = input().split(' ')
n, A, B = int(n), int(A), int(B)
s = [int(i) for i in input().split(' ')]
num = sum(s)
first = s[0]
after = s[1:]
after.sort()
rst = 0
ptr = len(after) - 1
while first / num < B / A:
    num -= after[ptr]
    ptr -= 1
    rst += 1
print(rst)
