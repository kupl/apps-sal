(N, K) = map(int, input().split())
(q, mod) = divmod(N, K)
mod_list = [mod]
while True:
    (q, mod) = divmod(q, K)
    mod_list.append(mod)
    if q <= 0:
        break
if mod_list[-1] == 0:
    result = len(mod_list) - 1
else:
    result = len(mod_list)
print(result)
