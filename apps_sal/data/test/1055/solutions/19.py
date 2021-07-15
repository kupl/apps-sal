kk=lambda:map(int,input().split())
ll=lambda:list(kk())
def dp(ls):
	if sorted(ls) == ls: return len(ls)
	return max(dp(ls[:len(ls)//2]), dp(ls[len(ls)//2:]))
_ = input(), print(dp(ll()))
