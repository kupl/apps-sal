n = int(input())
string = input()
word = "ogo" + "go" * 56
for i in range(57):
    #print(word, word in  string)
    string = string.replace(word, "***")
    word = word[:-2]
print(string)
