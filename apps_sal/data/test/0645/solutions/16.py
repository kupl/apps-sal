def R():
    return list(map(int, input().split(' ')))


s = input()
cnt = 0
for i in s:
    if i in 'aeiou' or i in '13579':
        cnt += 1
print(cnt)
