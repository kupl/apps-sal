s = "What are you doing at the end of the world? Are you busy? Will you save us?"
s1 = 'What are you doing while sending "'
s2 = '"? Are you busy? Will you send "'
s3 = '"?'
l1,l2,l3=len(s1),len(s2),len(s3)
def count(n):
    if n>=60:return 10**20
    return (1<<n)*75+((1<<n)-1)*68
def find(n,k):
    if count(n)<k:return '.'
    if n==0:return s[k-1]
    if k<=l1:return s1[k-1]
    c=count(n-1)
    k-=l1
    if k<=c:
        return find(n-1,k)
    k-=c
    if k<=l2:return s2[k-1]
    k-=l2
    if k<=c:
        return find(n-1,k)
    k-=c
    if k<=l3:return s3[k-1]
q=int(input())
ans=''
while q:
    n,k=map(int,input().split())
    while n > 70 and k > 34:
        k -= 34
        n -= 1
    if n > 0 and k <= 34: ans+=s1[k - 1]
    else :ans+=find(n,k)
    q-=1
print(ans)
