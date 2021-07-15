import sys,math,collections,itertools
input = sys.stdin.readline

N,M=list(map(int,input().split()))
#- 1要望 a→c,b→c分断要望に対して、a<bならb→cだけ考慮すればいい -#
want_list = [0]*(N+1)
for _ in range(M):
    a,b = list(map(int,input().split()))
    want_list[b]=max(want_list[b],a)


#-分断した時の橋とindexと要望を見比べて、要望を満たしていないならカウントする-#
cnt = 0
cutNo = 0
for idx,val in enumerate(want_list):
    if val >cutNo:
        cutNo = idx-1
        cnt += 1
print(cnt)


