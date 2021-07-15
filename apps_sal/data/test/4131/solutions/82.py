N,M=list(map(int,input().split()))
numbers=[{} for n in range(N)]
for m in range(M):
    P,Y=list(map(int,input().split()))
    numbers[P-1][m]=Y
answers={}
for n in range(N):
    number=numbers[n]
    if len(number)==0:
        continue
    new_number=sorted(list(number.items()), key=lambda x:x[1])
    suuji=1
    for num in new_number:
        answers[num[0]]=(6-len(str(n+1)))*'0'+str(n+1)+(6-len(str(suuji)))*'0'+str(suuji)
        suuji+=1
answer=sorted(list(answers.items()), key=lambda x:x[0])
for ans in answer:
    print((ans[1]))

