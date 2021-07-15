n, k, c = list(map(int, input().split()))
s = input()


cnt0 = [-10**10] * len(s)
cnt1 = [-10**10] * len(s)
rest0 = c
rest1 = c
ct0 = 1
ct1 = 1
for i in range(len(s)):
    a = s[i]
    b = s[len(s) - 1 - i]
    if (c <= rest0) & (a == 'o'):
        cnt0[i] = ct0
        ct0 += 1
        rest0 = 0
    else:
        rest0 += 1
    if (c <= rest1) & (b == 'o'):
        cnt1[len(s) - 1 - i] = ct1
        ct1 += 1
        rest1 = 0
    else:
        rest1 += 1
for i in range(len(s)):
    if (cnt0[i] + cnt1[i] == k+1):
        print((i+1))

