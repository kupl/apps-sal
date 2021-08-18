from operator import itemgetter
import sys
input = sys.stdin.readline


def compress(string):
    string.append("
    n=len(string)
    begin, end, cnt=0, 1, 1
    ans=[]
    while end < n:
        if string[begin] == string[end]:
            end, cnt=end + 1, cnt + 1
        else:
            ans.append((string[begin], cnt))
            begin, end, cnt=end, end + 1, 1
    return ans


t=int(input())
for _ in range(t):
    n=int(input())
    a=list(map(int, input().split()))
    a=sorted(a)
    comp=compress(a)
    comp=sorted(comp, key=itemgetter(1))
    same_max=comp[-1][-1]
    kind_max=len(comp)
    if same_max == kind_max:
        print(same_max - 1)
    else:
        print(min(same_max, kind_max))
