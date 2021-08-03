s = list(input())

for i in s:
    if s.count(i) > 1:
        print('no')
        break
else:
    print('yes')
