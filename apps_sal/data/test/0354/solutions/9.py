def solve(a, b):
    if len(a) != len(b):
        return False

    vowels = set(["a", "e", "i", "o", "u"])
    for index in range(len(a)):
        a_vowel = a[index] in vowels
        b_vowel = b[index] in vowels
        if a_vowel != b_vowel:
            return False

    return True 

a = input()
b = input()
if solve(a, b):
    print("Yes")
else:
    print("No")
