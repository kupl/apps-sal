(num_elements, num_queries) = list(map(int, input().split()))
elements = list(map(int, input().split()))
elements.sort(reverse=True)
occurrences = [0] * (num_elements + 2)
for _ in range(num_queries):
    (l, r) = list(map(int, input().split()))
    occurrences[l] += 1
    occurrences[r + 1] -= 1
for pos in range(1, num_elements + 1):
    occurrences[pos] += occurrences[pos - 1]
occurrences.sort(reverse=True)
solution = 0
for pos in range(num_elements):
    solution += occurrences[pos] * elements[pos]
print(solution)
