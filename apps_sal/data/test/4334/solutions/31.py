keys = list(map(str, input().split()))
values = list(map(int, input().split()))
rm_str = input()

dicts = {key: value for key, value in zip(keys, values)}
dicts[rm_str] = dicts[rm_str] - 1

print((' '.join([str(n) for n in list(dicts.values())])))

