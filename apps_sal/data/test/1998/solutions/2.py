n,a,b,k = map(int,input().split())
A=['1'] + list(input()) + ['1']
answer =[]
n+= 2
i = 0
while i <= n-2:
    per = 0
    for j in range(i+1, i+b+1):
        if j > n - 1:
            break
        if A[j] == '1':
            i = j
            per = 1
            break
    if per == 0:
        i = j
        answer.append(i)
lens = len(answer)
print(lens - a +1)
print(' '.join(map(str, answer[0:lens-a+1])))
