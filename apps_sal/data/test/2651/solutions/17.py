# solution
import io

data=lambda:list(map(int,input().split()))
data()
q=lambda x:sum(j*(len(x)-1-2*i)for i,j in enumerate(x))
print(q(data())*q(data())%(10**9+7))
