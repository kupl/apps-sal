s = list(input())
Le = len(s)//2
front = s[:Le+1]
back = s[-Le:]
count=0
for i in range(Le):
    if front[i] != back[-1-i]:
        count+=1
print(count)
