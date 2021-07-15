quiznum=int(input())
timeline=input().split(" ")
timeline=[int(n) for n in timeline]
#print(timeline)
time_0=0
for i in range(quiznum):
    time_0+=timeline[i]
#print(time_0)

medinum=int(input())
for i in range(medinum):
    temp_line=input().split(" ")
    a=int(temp_line[0])
    b=int(temp_line[1])
    time=time_0 - timeline[a-1] + b
    print(time)
