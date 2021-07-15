N = int(input())
texts = [0] * N
texts = input().split()

ends=set()
#print(ends)

ends.add(0)
#print(ends)

for i in range(N):
    if int(texts[i]) in ends:
        ends.remove(int(texts[i]))
        #print('-'+texts[i],end=' ')
    ends.add(i+1)
    #print(ends)

print(len(ends))


