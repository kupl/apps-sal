n, k = list(map(int, input().split()))
s = list(input())

if n == 1 and k>0:
    print(0)
    return


if k > 0 and s[0] != '1':
    s[0] = '1'
    k -= 1

i = 1


while k > 0 and i < n:
    if s[i] != '0':
        s[i] = '0'
        k -= 1
    i += 1

print(''.join(s))

