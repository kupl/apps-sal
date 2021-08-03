s = input()
k = int(input())
one_cnt = 0

for i in range(len(s)):
    if s[i] == '1':
        one_cnt += 1
    else:
        break

if k <= one_cnt:
    print(1)
    return

for i in range(len(s)):
    if s[i] != '1':
        print(s[i])
        return
