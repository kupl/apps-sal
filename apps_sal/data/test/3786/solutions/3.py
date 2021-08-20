n = int(input().strip())
count = [0] * n
params = [-1, 0] + list(map(int, input().split()))
i = 2
layer = [0] * (n + 1)
nodes_in_layer = {}
while i <= n:
    layer[i] = layer[params[i]] + 1
    count[params[i]] += 1
    if nodes_in_layer.get(layer[i]) is None:
        nodes_in_layer.setdefault(layer[i], 1)
    else:
        nodes_in_layer[layer[i]] += 1
    i += 1
max_layer = max(layer)
result = 1
for i in range(1, max_layer + 1):
    result += nodes_in_layer[i] % 2
print(result)
