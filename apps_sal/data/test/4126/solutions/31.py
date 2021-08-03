S = input()


class Palindrome:
    def __init__(self, string):
        self.string = string

    def jugde_paindrome(self):
        if self.string == self.string[::-1]:
            return True
        else:
            return False


before = S[:int((len(S) - 1) / 2)]
after = S[int((len(S) - 1) / 2) + 1:]
S_judge = Palindrome(S)
before_judge = Palindrome(before)
after_judge = Palindrome(after)

if S_judge.jugde_paindrome() == True and after_judge.jugde_paindrome() == True and before_judge.jugde_paindrome() == True:
    print("Yes")
else:
    print("No")
