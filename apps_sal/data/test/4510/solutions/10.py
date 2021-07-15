from collections import OrderedDict
class LRUCache:

    def __init__(self, capacity):
        self.capacity = capacity
        self.cache = OrderedDict()

    def set(self, key, value):
        if len(self.cache) == self.capacity:
            self.cache.popitem(last=False)
        self.cache[key] = value

n, k = map(int, input().strip().split())
ids = map(int, input().strip().split())
convs = LRUCache(k)
for i in ids:
    if i in convs.cache:
        continue
    else:
        convs.set(i, None)
print(len(convs.cache))
print(" ".join(map(str, reversed(convs.cache.keys()))))
