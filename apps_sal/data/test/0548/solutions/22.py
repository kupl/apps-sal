input()
for t in input().split():
    if int(t) % 2:
        print('First')
        break
else:
    print('Second')
