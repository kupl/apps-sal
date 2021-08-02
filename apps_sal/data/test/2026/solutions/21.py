n = int(input())
s = input()
mh = ''
mv = ''
count = 0
for e in s:
    if mv == '' and e in ('U', 'D'):
        mv = e
    if mh == '' and e in ('L', 'R'):
        mh = e
    if e in ('U', 'D'):
        if e != mv:
            count += 1
            mv = e
            mh = ''
    if e in ('L', 'R'):
        if e != mh:
            count += 1
            mh = e
            mv = ''

print(count + 1)
