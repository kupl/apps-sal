a, b, k = map(int, input().split())

takahashi_list = [0, a-k] 
aoki_list = [0, b + min(takahashi_list)]

print(max(takahashi_list), max(aoki_list))
