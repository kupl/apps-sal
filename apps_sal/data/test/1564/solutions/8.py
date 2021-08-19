n = int(input())
s = input()
t = input()
b_a = 0
ba = []
a_b = 0
ab = []
for i in range(n):
    if s[i] == 'a' and t[i] == 'b':
        a_b += 1
        ab.append(i)
    if s[i] == 'b' and t[i] == 'a':
        b_a += 1
        ba.append(i)
ans = -1
if a_b % 2 == b_a % 2:
    ans = a_b // 2 + b_a // 2
    ans += 2 * (a_b % 2)
    print(ans)
    for i in range(1, len(ab), 2):
        print(ab[i - 1] + 1, ab[i] + 1)
    for i in range(1, len(ba), 2):
        print(ba[i - 1] + 1, ba[i] + 1)
    if a_b % 2 != 0:
        print(ab[-1] + 1, ab[-1] + 1)
        print(ab[-1] + 1, ba[-1] + 1)
if ans == -1:
    print(ans)
