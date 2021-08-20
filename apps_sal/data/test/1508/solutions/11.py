n = int(input())
list1 = list(map(int, input().split()))
print(max(list1), ' '.join(map(str, sorted(list1)[1:-1])), min(list1))
