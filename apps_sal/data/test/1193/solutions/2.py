import heapq
n, uch = list(map(int, input().split()))
speeds = list(map(int, input().split()))

godnie = heapq.nlargest(uch, speeds)
print(min(godnie))
