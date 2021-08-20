elements = '1\tH\tHydrogen\n2\tHe\tHelium\n3\tLi\tLithium\n4\tBe\tBeryllium\n5\tB\tBoron\n6\tC\tCarbon\n7\tN\tNitrogen\n8\tO\tOxygen\n9\tF\tFluorine\n10\tNe\tNeon\n11\tNa\tSodium\n12\tMg\tMagnesium\n13\tAl\tAluminum\n14\tSi\tSilicon\n15\tP\tPhosphorus\n16\tS\tSulfur\n17\tCl\tChlorine\n18\tAr\tArgon\n19\tK\tPotassium\n20\tCa\tCalcium\n21\tSc\tScandium\n22\tTi\tTitanium\n23\tV\tVanadium\n24\tCr\tChromium\n25\tMn\tManganese\n26\tFe\tIron\n27\tCo\tCobalt\n28\tNi\tNickel\n29\tCu\tCopper\n30\tZn\tZinc\n31\tGa\tGallium\n32\tGe\tGermanium\n33\tAs\tArsenic\n34\tSe\tSelenium\n35\tBr\tBromine\n36\tKr\tKrypton\n37\tRb\tRubidium\n38\tSr\tStrontium\n39\tY\tYttrium\n40\tZr\tZirconium\n41\tNb\tNiobium\n42\tMo\tMolybdenum\n43\tTc\tTechnetium\n44\tRu\tRuthenium\n45\tRh\tRhodium\n46\tPd\tPalladium\n47\tAg\tSilver\n48\tCd\tCadmium\n49\tIn\tIndium\n50\tSn\tTin\n51\tSb\tAntimony\n52\tTe\tTellurium\n53\tI\tIodine\n54\tXe\tXenon\n55\tCs\tCesium\n56\tBa\tBarium\n57\tLa\tLanthanum\n58\tCe\tCerium\n59\tPr\tPraseodymium\n60\tNd\tNeodymium\n61\tPm\tPromethium\n62\tSm\tSamarium\n63\tEu\tEuropium\n64\tGd\tGadolinium\n65\tTb\tTerbium\n66\tDy\tDysprosium\n67\tHo\tHolmium\n68\tEr\tErbium\n69\tTm\tThulium\n70\tYb\tYtterbium\n71\tLu\tLutetium\n72\tHf\tHafnium\n73\tTa\tTantalum\n74\tW\tTungsten\n75\tRe\tRhenium\n76\tOs\tOsmium\n77\tIr\tIridium\n78\tPt\tPlatinum\n79\tAu\tGold\n80\tHg\tMercury\n81\tTl\tThallium\n82\tPb\tLead\n83\tBi\tBismuth\n84\tPo\tPolonium\n85\tAt\tAstatine\n86\tRn\tRadon\n87\tFr\tFrancium\n88\tRa\tRadium\n89\tAc\tActinium\n90\tTh\tThorium\n91\tPa\tProtactinium\n92\tU\tUranium\n93\tNp\tNeptunium\n94\tPu\tPlutonium\n95\tAm\tAmericium\n96\tCm\tCurium\n97\tBk\tBerkelium\n98\tCf\tCalifornium\n99\tEs\tEinsteinium\n100\tFm\tFermium\n101\tMd\tMendelevium\n102\tNo\tNobelium\n103\tLr\tLawrencium\n104\tRf\tRutherfordium\n105\tDb\tDubnium\n106\tSg\tSeaborgium\n107\tBh\tBohrium\n108\tHs\tHassium\n109\tMt\tMeitnerium\n110\tDs\tDarmstadtium\n111\tRg\tRoentgenium\n112\tCn\tCopernicium\n113\tNh\tNihonium\n114\tFl\tFlerovium\n115\tMc\tMoscovium\n116\tLv\tLivermorium\n117\tTs\tTennessine\n118\tOg\tOganesson\n'.strip().split('\n')
elements = [line.split()[1].upper() for line in elements]


def isPossible(s):
    if s in elements:
        return True
    for e in elements:
        if s.startswith(e) and isPossible(s[len(e):]):
            return True
    return False


S = input()
if isPossible(S):
    print('YES')
else:
    print('NO')
