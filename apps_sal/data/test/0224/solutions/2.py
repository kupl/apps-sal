3

vowels = ['A', 'E', 'I', 'O', 'U', 'Y']
s = 'A' + input() + 'A'

arr = [i for i in range(len(s)) if s[i] in vowels]
diffs = [arr[i + 1] - arr[i] for i in range(len(arr) - 1)]

print(max(diffs))
