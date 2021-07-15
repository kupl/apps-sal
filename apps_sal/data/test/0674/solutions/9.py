StringsNumber = int(input())
FinalStrings = []
Strings = []

for i in range(StringsNumber):
    Strings.append(input())

LetterGraph = {}

# Генерим граф

for i in range(len(Strings)):
    if len(Strings[i]) == 1:
        if Strings[i] not in LetterGraph:
            LetterGraph[Strings[i]] = ""
            #print("заапедил", i)
        continue
    for e in range(len(Strings[i]) - 1):
        if Strings[i][e] not in LetterGraph:
            Elements = []
            for j in list(LetterGraph):
                if j != Strings[i][e + 1]:
                    Elements.append(LetterGraph[j])

            if Strings[i][e + 1] in Elements:
                print("NO")
                return
            LetterGraph[Strings[i][e]] = Strings[i][e + 1]
            continue
        if LetterGraph[Strings[i][e]] == Strings[i][e + 1] or LetterGraph[Strings[i][e]] == "":
            LetterGraph[Strings[i][e]] = Strings[i][e + 1]
            continue
        #print("Граф:", LetterGraph)
        print("NO")
        return

#print("Я сгенерил граф, получилось:", LetterGraph)

# Проверяем, что нету цикла

if LetterGraph:
    Cycle = False
    for i in LetterGraph:
        Letter = LetterGraph[i]
        while True:
            if Letter in LetterGraph:
                if LetterGraph[Letter] == i:
                    print("NO")
                    return
                Letter = LetterGraph[Letter]

            else:
                break

# Находим возможные первые символы

if LetterGraph:
    IsIFirstSymbol = False
    FirstSymbols = []

    for i in LetterGraph:
        IsIFirstSymbol = True
        for e in LetterGraph:
            if LetterGraph[e] == i:
                #print(i, "не подходит, потому что", e, "указывает на него.")
                IsIFirstSymbol = False
        if IsIFirstSymbol:
            FirstSymbols.append(i)

    if not FirstSymbols:
        print("NO")
        return

#print("Варианты первого символа:", *FirstSymbols)

# Создаем варианты финальной строки

if LetterGraph:
    Letter = ""
    for i in FirstSymbols:
        FinalString = i
        Letter = i
        for e in range(len(LetterGraph)):
            if Letter in LetterGraph:
                if not (LetterGraph[Letter] == ""):
                    FinalString += LetterGraph[Letter]
                    #print(Letter, "есть в графе, так что добавляем", LetterGraph[Letter], ", на которое оно указывает.")
                    Letter = LetterGraph[Letter]
                else:
                    break
            else:
                break

        FinalStrings.append(FinalString)

#print("Отдельные строки", *FinalStrings)

FinalStrings.sort()

RESULT = ""

for i in FinalStrings:
    RESULT += i

print(RESULT)

