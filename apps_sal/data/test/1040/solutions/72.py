n = int(input())
s = input()


work = ''

for i in s:
    work += i
    if work[-3:] == 'fox':
        work = work[:-3]
print(len(work))
