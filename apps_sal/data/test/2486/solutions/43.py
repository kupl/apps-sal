N, K = list(map(int, input().split()))
a = list(map(int, input().split()))
a = sorted(a)
ans = N
psum = 0
for i in range(N-1, -1, -1) :
    if psum+a[i] < K :
        psum += a[i]
    else :
        ans = min(ans, i)
print(ans)

'''
notes:
1-->we include elems that are less than k  
2-->if some x is necessary all elems grtr than x are also necessary 
Base for some x to be necessary:: 
     atleast one of the sums in range [sm-x,sm) must be possible 
     excluding x  
now at any instance after traversing x elements 
we make sure that we have max posible sm <k 
now 
if x+sm <k 
    we cannot include this anyway 
otherwise
    we can make a set with {sm,x} now x is important 
BOOYAH (:
'''

