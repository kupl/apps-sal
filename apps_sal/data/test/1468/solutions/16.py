def cut_to_lexicographic(word_bigger, word_smaller):
    if word_bigger <= word_smaller:
        return word_bigger
    for l in range(len(word_bigger)):
        if word_bigger[l] != word_smaller[l]:
            return word_bigger[:l]
    return word_bigger


n = int(input())
array = [str(input()) for c in range(n)]
b = n - 2
while b > -1:
    if array[b + 1] >= array[b]:
        b = b - 1
    else:
        if len(array[b]) > len(array[b + 1]):
            array[b] = array[b][:len(array[b + 1])]
        array[b] = cut_to_lexicographic(array[b], array[b + 1])
print('\n'.join(array))
