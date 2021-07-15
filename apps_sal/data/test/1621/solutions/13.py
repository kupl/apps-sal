alpha = {'a':1, 'b':2 ,'c': 3,'d':4,'e':5 ,'f':6 ,'g':7 ,'h':8,'i':9,'j':10,'k':11,'l':12,'m':13,'n':14,'o':15,'p':16,'q':17,'r':18,'s':19,'t':20,'u':21,'v':22,
         'w':23,'x':24,'y':25,'z':26}
s = input()
k = int(input())
score = list(map(int,input().split()))
score1 = list(score)
score.sort(reverse = True)

value = 0
for i in range(len(s)):
    value += score1[alpha[s[i]]-1]*(i+1)
    #print(value)
for i in range(len(s)+1,len(s)+1+k):
    value += score[0]*i
print(value)

