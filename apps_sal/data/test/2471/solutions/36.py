def solve(h,w,n,black_list):
  if len(black_list) == 0:
    return [(h-2)*(w-2)]+[0]*9
  idx_list = []
  for idx, (a,b) in enumerate(black_list):
    left = max(0, b-3)
    top = max(0, a-3)
    for row in range(top, a):
      if row+2 >= h:
        continue
      for col in range(left, b):
        if col+2 >= w:
          continue
        idx_list.append(row*w+col)

  set_count = set(idx_list)
  idx_list = sorted(idx_list)

  ans = [0]*9
  now = idx_list[0]
  count = 0
  for item in idx_list:
    if item == now:
      count += 1
    else:
      now = item
      if count == 10:
        print(item)
      ans[count-1] += 1
      count = 1
  ans[count-1] += 1
  return [(h-2)*(w-2)-len(set_count)]+ans


def __starting_point():
  h,w,n = list(map(int,input().split()))
  black_list = [tuple(map(int,input().split())) for _ in range(n)]
  ret = solve(h,w,n,black_list)
  for i in ret:
    print(i)

__starting_point()
