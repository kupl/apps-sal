(N, K) = list(map(int, input().split()))
a = list(map(int, input().split()))
a = sorted(a)
ans = N
psum = 0
for i in range(N - 1, -1, -1):
    if psum + a[i] < K:
        psum += a[i]
    else:
        ans = min(ans, i)
print(ans)
'\nnotes:\n1-->we include elems that are less than k  \n2-->if some x is necessary all elems grtr than x are also necessary \nBase for some x to be necessary:: \n     atleast one of the sums in range [sm-x,sm) must be possible \n     excluding x  \nnow at any instance after traversing x elements \nwe make sure that we have max posible sm <k \nnow \nif x+sm <k \n    we cannot include this anyway \notherwise\n    we can make a set with {sm,x} now x is important \nBOOYAH (:\n'
