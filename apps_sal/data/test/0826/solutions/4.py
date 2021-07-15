import sys

# B - log
def is_match(k):
	# 条件が"xx未満"の場合、ここの不等号を変える
	if (1+k)*k//2 <= n+1:
		return True
	else:
		return False


n = int(input())

left = -1
right = n+1

# リストが単調増加,単調減少どっちでも この書き方でOK
while right - left > 1:
  mid = (left + right) // 2
  #print(left, right, mid)

  if is_match(mid):
    left = mid
  else:
    right = mid

print(n-left+1)
