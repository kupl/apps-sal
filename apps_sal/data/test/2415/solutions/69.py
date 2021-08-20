s = '\n\nHydrogen\tH\tNiobium\tNb\tThallium\tTl\nHelium\tHe\tMolybdenum\tMo\tLead\tPb\nLithium\tLi\tTechnetium\tTc\tBismuth\tBi\nBeryllium\tBe\tRuthenium\tRu\tPolonium\tPo\nBoron\tB\tRhodium\tRh\tAstatine\tAt\nCarbon\tC\tPalladium\tPd\tRadon\tRn\nNitrogen\tN\tSilver\tAg\tFrancium\tFr\nOxygen\tO\tCadmium\tCd\tRadium\tRa\nFluorine\tF\tIndium\tIn\tActinium\tAc\nNeon\tNe\tTin\tSn\tThorium\tTh\nSodium\tNa\tAntimony\tSb\tProtactinium\tPa\nMagnesium\tMg\tTellurium\tTe\tUranium\tU\nAluminum\tAl\tIodine\tI\tNeptunium\tNp\nSilicon\tSi\tXenon\tXe\tPlutonium\tPu\nPhosphorus\tP\tCesium\tCs\tAmericium\tAm\nSulfur\tS\tBarium\tBa\tCurium\tCm\nChlorine\tCl\tLanthanum\tLa\tBerkelium\tBk\nArgon\tAr\tCerium\tCe\tCalifornium\tCf\nPotassium\tK\tPraseodymium\tPr\tEinsteinium\tEs\nCalcium\tCa\tNeodymium\tNd\tFermium\tFm\nScandium\tSc\tPromethium\tPm\tMendelevium\tMd\nTitanium\tTi\tSamarium\tSm\tNobelium\tNo\nVanadium\tV\tEuropium\tEu\tLawrencium\tLr\nChromium\tCr\tGadolinium\tGd\tRutherfordium\tRf\nManganese\tMn\tTerbium\tTb\tDubnium\tDb\nIron\tFe\tDysprosium\tDy\tSeaborgium\tSg\nCobalt\tCo\tHolmium\tHo\tBohrium\tBh\nNickel\tNi\tErbium\tEr\tHassium\tHs\nCopper\tCu\tThulium\tTm\tMeitnerium\tMt\nZinc\tZn\tYtterbium\tYb\tDarmstadtium\tDs\nGallium\tGa\tLutetium\tLu\tRoentgenium\tRg\nGermanium\tGe\tHafnium\tHf\tCopernicium\tCn\nArsenic\tAs\tTantalum\tTa\tNihonium\tNh\nSelenium\tSe\tTungsten\tW\tFlerovium\tFl\nBromine\tBr\tRhenium\tRe\tMoscovium\tMc\nKrypton\tKr\tOsmium\tOs\tLivermorium\tLv\nRubidium\tRb\tIridium\tIr\tTennessine\tTs\nStrontium\tSr\tPlatinum\tPt\tOganesson\tOg\nYttrium\tY\tGold\tAu\nZirconium\tZr\tMercury\tHg\n'
elems = []
for (idx, token) in enumerate(s.split()):
    if idx % 2 == 1:
        elems.append(token.upper())


def check(s):
    if not s:
        return True
    for idx in range(len(s)):
        if s[idx:] in elems and check(s[:idx]):
            return True
    return False


s = input()
if check(s):
    print('YES')
else:
    print('NO')
