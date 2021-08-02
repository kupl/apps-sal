import heapq
n, uch = list(map(int, input().split()))
speeds = list(map(int, input().split()))
# n - kompi
# na i kompe skorost' a[i]
# uch uchastnikov
# orgi hot'yat ravn skorost' no max

godnie = heapq.nlargest(uch, speeds)
print(min(godnie))
