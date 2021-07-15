K=int(input())
K1=K//50
K2=K%50

answer_list=[]
for i in reversed(range(50-K2)):
  answer_list.append(i)
for i in range(K2):
  answer_list.append(50-i)
#print(answer_list)

for i in range(50):
  answer_list[i]+=K1

print(50)
print(*answer_list)
