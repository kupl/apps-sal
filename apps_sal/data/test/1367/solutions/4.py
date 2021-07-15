n=int(input())
ser={ i for i in range(1,1+n)}
smotr=set(map(int, input().split()))
for i in ser:
    if i not in smotr:
        print(i)
        break

