import sys


def make_gen(str):
    arr = str.split(' ')
    for item in arr:
        yield item


s = input()
s = make_gen(s)
n = next(s)
k = int(next(s))
count = 0
deleted = 0
for i in range(0, len(n)):
    if n[-i - 1] == '0':
        count += 1
        if count == k:
            break
    else:
        deleted += 1
if count < k:
    if count > 0:
        print(len(n) - 1)
    else:
        print(len(n))
else:
    print(deleted)
