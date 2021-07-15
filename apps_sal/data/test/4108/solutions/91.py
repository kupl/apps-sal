s=list(input())
t=list(input())
n=len(s)
def get_count_list(s):
    alphabets="abcdefghijklmnopqrstuvwxyz"
    ans={}
    for alphabet in alphabets:
        ans[alphabet]=[]
    for i in range(n):
        ans[s[i]].append(i)
    return ans


def get_index2alpha(s):
    ans={}
    for i in range(n):
        ans[i]=s[i]
    return ans

s_count=get_count_list(s)
t_count=get_count_list(t)
s_index=get_index2alpha(s)
t_index=get_index2alpha(t)

ans=0

s_set=set(s)


for i in range(n):
    s_alpha=s_index[i]
    t_alpha = t_index[i]
    if s_alpha in s_set:
        s_set.remove(s_alpha)
        if not s_count[s_alpha]==t_count[t_alpha]:
            ans+=1

if ans==0:
    print("Yes")
else:
    print("No")
