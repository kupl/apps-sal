n, k = map(int, input().split())

r, s, p = map(int, input().split())

t = input()

li = list(t[:k])

cnt = 0

for itr, val in enumerate(t):

  if itr >= k and val == li[itr % k]:

    li[itr % k] = "x"

  else:

    if val == "r":

      cnt += p

    elif val == "s":

      cnt += r

    else:

      cnt += s

    li[itr % k] = val

print(cnt)
