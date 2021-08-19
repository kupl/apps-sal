s = input()
cnt = sum((s.count(i) % 2 for i in s))
if cnt % 2 == 1 or cnt == 0:
    print('First')
else:
    print('Second')
