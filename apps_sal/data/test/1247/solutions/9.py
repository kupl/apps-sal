import sys

mem = {}

def palindrome_set_counts(string):
    if string == "":
        return True
    
    counts = {}
    for letter in string:
        if letter not in counts:
            counts[letter] = 0
        counts[letter] += 1
        counts[letter] %= 2

    letter_sums = 0
    for key, value in list(counts.items()):
        letter_sums += value

    return letter_sums

def who_wins():
    results = [1, 1, -1, 1]
    for i in range(4, 2000000):
        results.append(results[i-1] * -1)

    return results

counts = palindrome_set_counts(sys.stdin.readline().strip())
print("First" if who_wins()[counts] == 1 else "Second")
        

